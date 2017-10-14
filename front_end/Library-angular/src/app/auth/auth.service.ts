import { Injectable } from '@angular/core';
import { Headers, Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import { Subject } from 'rxjs/Subject';
// import 'rxjs/add/operator/toPromise';
import 'rxjs/Rx';

import { User } from '../models/user.model';
//-----------------------------------------------

@Injectable()
export class AuthService{

  loggedUser = new Subject();
  private mainUrl = 'http://127.0.0.1:8000';

  constructor(private http: Http){}
  //...........................................................................
  register(newUser: any){
    let url = this.mainUrl +'/api/users/register/?format=json'
    let headers = new Headers();
    //headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.post(url, newUser, headers)
      .map(
        (response: Response) => {
          const data = response.json();
          return data;
        }
      )
      .catch(
        (error: Response) => {
          return Observable.throw("your username is repeatitious. Please select another username.");
        }
      );
  }
  //...........................................................................
  login(aUser: any){
    let url = this.mainUrl + '/api/users/login/?format=json';
    let headers = new Headers();
    //headers.append('Authorization', 'Your token used in app');
    headers.append('Content-Type', 'application/json');
    headers.append('Access-Control-Allow-Origin', '*');

    return this.http.post(url, aUser, headers)
    .map(
      (response: Response) => {
        const data = response.json();
        return data;
      }
    )
    .catch(
      (error: Response) => {
        return Observable.throw("username and password are not valid!");
      }
    );
  }
}
