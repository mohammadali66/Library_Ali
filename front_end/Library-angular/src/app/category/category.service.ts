import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class CategoryService{
  private mainUrl = 'http://127.0.0.1:8000';

  constructor(private http: Http){}
  //...........................................................................
  getCategoryBooksHomeList(){
    let url = this.mainUrl + '/api/books/categorybookshome/?format=json';
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(url, headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );
  }
  //...........................................................................
  getCategoryMenu(){
    let url = this.mainUrl + '/api/books/categorymenu/?format=json';
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(url, headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );
  }
  //...........................................................................
  getOneCategoryByBooks(categorySlug: string){
    let headers = new Headers();
    headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(this.mainUrl + '/category/' + categorySlug + '/?format=json', headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );
  }
}
