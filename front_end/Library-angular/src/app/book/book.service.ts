import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class BookService{
  url = 'http://127.0.0.1:8000';
  constructor(private http: Http){}

  getBookDetail(slug: string){
    //let book: any;
    let headers = new Headers();
    headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(this.url + '/book/' + slug + '/?format=json', headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );

  }
}
