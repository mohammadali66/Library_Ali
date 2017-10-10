import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class CategoryService{
  url = 'http://127.0.0.1:8000';

  constructor(private http: Http){}

  getCategoryList(){
    let headers = new Headers();
    headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(this.url + '/categoryall/?format=json', headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );
  }

  getOneCategoryByBooks(categorySlug: string){
    let headers = new Headers();
    headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.get(this.url + '/category/' + categorySlug + '/?format=json', headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      );
  }
}
