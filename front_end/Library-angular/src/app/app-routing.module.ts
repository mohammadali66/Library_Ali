import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";

import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './auth/registration/registration.component';
import { BookDetailComponent } from './book/book-detail/book-detail.component';
import { CategoryDetailComponent } from './category/category-detail/category-detail.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'register', component: RegistrationComponent },
  { path: 'book', children:[
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
