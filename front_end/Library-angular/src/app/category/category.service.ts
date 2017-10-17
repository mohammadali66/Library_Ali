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
  getOneCategoryBrief(categorySlug: string){
    let url = this.mainUrl + '/api/books/categorybrief/' + categorySlug + '/?format=json';
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
  //get books list of a category
  getBooksOfOneCategory(categorySlug: string, pageUrl=null){
    let url: string = '';
    if(!pageUrl){
        url = this.mainUrl + '/api/books/bookscategory/' + categorySlug + '/?format=json';
    }else{
      url = pageUrl;
    }

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
}
