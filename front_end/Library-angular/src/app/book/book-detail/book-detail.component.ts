import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Subscription } from 'rxjs/Subscription';

import { BookService } from '../book.service';
import { Book } from '../../models/book.model';

@Component({
  selector: 'app-book-detail',
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.css']
})
export class BookDetailComponent implements OnInit, OnDestroy {
  //slugSubscription: Subscription;
  //apiSubscription: Subscription;

  book: Book = new Book;
  pageNumber = 1;
  pdfFilePath: string;
  isLoggedUser = false;

  constructor(private bookService: BookService, private route: ActivatedRoute) { }

  ngOnInit() {
    //get slug from url
    this.route.params.subscribe(
      (params: Params) => {
        this.book.slug = params['slug'];

        //get book from API
        this.bookService.getBookDetail(this.book.slug)
          .subscribe(
            (bookData) => {
              console.log(bookData);

              this.book.title = bookData.title;
              this.book.slug = bookData.slug;
              this.book.description = bookData.description;
              this.book.authors = bookData.authors;
              this.book.publisher = bookData.publisher;
              this.book.pageCount = bookData.pageCount;
              this.book.image = bookData.image;

              this.book.pdfFile = bookData.pdfFile;
              this.pdfFilePath = this.bookService.mainUrl + bookData.pdfFile;

              //this.book.featured = bookData.featured;
              this.book.category = bookData.category;

              //is logged user
              if(localStorage.getItem('token') !== '')
                this.isLoggedUser = true
              else
                this.isLoggedUser = false;
            },
            (error) => console.log(error)
          );
      }
    );



  }

  leftPage(){
    this.pageNumber = this.pageNumber - 1;
    if(this.pageNumber <= 1){
      this.pageNumber = 1;
    }
  }

  rightPage(){
    this.pageNumber = this.pageNumber + 1;
    if(this.pageNumber >= this.book.pageCount){
      this.pageNumber = this.book.pageCount;
    }

  }

  ngOnDestroy(){
    //this.slugSubscription.unsubscribe();
    //this.apiSubscription.unsubscribe();
  }

}
