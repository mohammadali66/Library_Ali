import { Component, OnInit } from '@angular/core';

import { AuthService } from './auth/auth.service';
import { User } from './models/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'app';
  myToken = 'not found';
  //token2 = 'token 2: ';

  constructor(private authService: AuthService){}

  ngOnInit(){
    this.myToken = localStorage.getItem('token');
    this.authService.loggedUser.subscribe(
      (token: string) => {
        this.myToken = token;
      }
    );
  }
}
