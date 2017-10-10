import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BaseComponent } from './base/base.component';
import { NavigationComponent } from './base/navigation/navigation.component';
import { FooterComponent } from './base/footer/footer.component';
import { HomeComponent } from './home/home.component';
import { RegistrationComponent } from './auth/registration/registration.component';
import { AuthService } from './auth/auth.service';
import { BookDetailComponent } from './book/book-detail/book-detail.component';
import { BookService } from './book/book.service';
import { PdfViewerComponent } from 'ng2-pdf-viewer';
import { CategoryListComponent } from './category/category-list/category-list.component';
import { CategoryService } from './category/category.service';
import { CategoryDetailComponent } from './category/category-detail/category-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    BaseComponent,
    NavigationComponent,
    FooterComponent,
    HomeComponent,
    RegistrationComponent,
    BookDetailComponent,
    PdfViewerComponent,
    CategoryListComponent,
    CategoryDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [AuthService, BookService, CategoryService],
  bootstrap: [AppComponent]
})
export class AppModule { }
