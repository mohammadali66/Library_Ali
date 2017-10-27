import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './auth/registration/registration.component';
import { LoginComponent } from './auth/login/login.component';
import { BookDetailComponent } from './book/book-detail/book-detail.component';
import { BooksUserComponent } from './book/books-user/books-user.component';
import { CategoryDetailComponent } from './category/category-detail/category-detail.component';
import { NoteCreateComponent } from './note/note-create/note-create.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },  

  { path: 'users', children: [
    { path: 'register', component: RegistrationComponent }
    //{ path: 'login',    component: LoginComponent },
  ]},

  { path: 'book', children:[
    {path: 'mylibrary', component: BooksUserComponent },
    { path: ':slug', component: BookDetailComponent }
  ] },

  {path: 'category', children:[
    {path: ':categoryslug', component: CategoryDetailComponent }
  ]}
];

@NgModule({
  imports:[
    RouterModule.forRoot(appRoutes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule{}
