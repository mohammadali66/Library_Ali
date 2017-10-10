import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

import { AuthService } from '../auth.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  private errorMessage: string = 'errorrrrr'
  private successMessage: string;
  constructor(private authService: AuthService) { }

  ngOnInit() {
  }

  registerUser(form: NgForm){
    let user = {
      first_name: form.value.first_name,
      last_name: form.value.last_name,
      username: form.value.username,
      email: form.value.email,
      password: form.value.password
    }

    this.authService.register(user)
        .subscribe(
          (data: any[]) => {
            //console.log(data);
            this.successMessage = "created successfully";
          },
          (error) => {
            this.errorMessage = error;
          }
        );
  }
}
