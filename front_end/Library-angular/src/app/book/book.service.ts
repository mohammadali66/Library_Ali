import { Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class BookService{
  mainUrl = 'http://127.0.0.1:8000';
  constructor(private http: Http){}

  getBookDetail(slug: string){
    let url = this.mainUrl + '/api/books/bookdetail/' + slug + '/?format=json';
    let headers = new Headers();

    if(localStorage.getItem('token') !== ''){
      headers = new Headers({ 'Authorization': 'Token ' + localStorage.getItem('token') });
    }else{
      headers = new Headers({});
    }
    let options = new RequestOptions({ headers: headers });

    return this.http.get(url, options)
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



  // getBookDetail(slug: string){
  //   let url = this.mainUrl + '/api/books/bookdetail/' + slug + '/?format=json';
  //   let headers = new Headers();
  //   console.log('Token ' + localStorage.getItem('token'));
  //   headers.append('Authorization', 'Token ' + localStorage.getItem('token'));
  //   headers.append('Content-Type', 'application/json');
  //   headers.append('Access-Control-Allow-Origin', '*');
  //
  //   //let options = new RequestOptions({ headers: headers });
  //
  //   return this.http.get(url, headers)
  //   //return this.http.get(url, options)
  //     .map(
  //       (response: Response) => {
  //         const data = response.json();
  //         return data;
  //       }
  //     )
  //     .catch(
  //       (error: Response) => {
  //         return Observable.throw(error);
  //         //return Observable.throw('Not Found!!');
  //       }
  //     );
  // }
}
