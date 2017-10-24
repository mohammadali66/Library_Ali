import { Injectable } from '@angular/core';
import { Headers, Http, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs';

@Injectable()
export class NoteService{
  private mainUrl = 'http://127.0.0.1:8000';

  constructor(private http: Http){}
  //...........................................................................
  createNote(bookslug: string, newNote: any){
    let url = this.mainUrl + '/api/books/note/' + bookslug + '/?format=json';
    let headers = new Headers();

    if(localStorage.getItem('token') !== ''){
      headers = new Headers({ 'Authorization': 'Token ' + localStorage.getItem('token') });
    }else{
      headers = new Headers({});
    }
    let options = new RequestOptions({ headers: headers });

    return this.http.post(url, newNote, options)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      )
      .catch(
        (error: Response) => {
          return Observable.throw(error);
          //return Observable.throw('Not Found!!');
        }
      );
  }

  //...........................................................................
  deleteNote(pk: any){
    let url = this.mainUrl + '/api/books/noteupdatedelete/' + pk + '/?format=json';
    let headers = new Headers();

    if(localStorage.getItem('token') !== ''){
      headers = new Headers({ 'Authorization': 'Token ' + localStorage.getItem('token') });
    }else{
      headers = new Headers({});
    }
    let options = new RequestOptions({ headers: headers });

    return this.http.delete(url, options)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      )
      .catch(
        (error: Response) => {
          return Observable.throw(error);
          //return Observable.throw('Not Found!!');
        }
      );
  }
}
