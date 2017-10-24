import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { CKEditorModule } from 'ng2-ckeditor';

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
import { LoginComponent } from './auth/login/login.component';
import { NoteCreateComponent } from './note/note-create/note-create.component';
import { NoteService } from './note/note.service';

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
    CategoryDetailComponent,
    LoginComponent,
    NoteCreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule,
    CKEditorModule
  ],
  providers: [AuthService, BookService, CategoryService, NoteService],
  bootstrap: [AppComponent]
})
export class AppModule { }
