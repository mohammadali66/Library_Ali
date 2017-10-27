import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../auth.service';
import { User } from '../../models/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loggedUsername: string = '';
  errorMessage = '';

  constructor(private authService: AuthService,
              private router: Router) { }

  ngOnInit() {
    if(localStorage.getItem('username')){
        this.loggedUsername = localStorage.getItem('username');
    }
  }
  //....................................................................
  //login user method
  loginUser(form: NgForm){
    let myUser = {
      username: form.value.username,
      password: form.value.password
    }

    this.authService.login(myUser)
      .subscribe(
        (data: any) => {
          localStorage.setItem('token', data.token);
          localStorage.setItem('username', myUser.username);
          this.loggedUsername = localStorage.getItem('username');
          //console.log(this.router.url);
          this.errorMessage = '';
          this.router.navigate([this.router.url]);
          window.location.reload();
          // let user = new User();
          // user.username = myUser.username;
          // user.token = data.token;
          // this.authService.loggedUser.next(user)
          //this.authService.loggedUser.next(localStorage.getItem('token'))
        },
        (error) => {
          //console.log(error);
          this.errorMessage = error;
        }
      );
  }
  //....................................................................
  //logout user method
  logoutUser(){
    localStorage.setItem('token', '');
    localStorage.setItem('username', '');
    this.loggedUsername = null;

    window.location.reload();
  }
}
