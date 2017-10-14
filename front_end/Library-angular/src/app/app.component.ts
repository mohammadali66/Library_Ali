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


  constructor(private authService: AuthService){}

  ngOnInit(){
    
  }
}
