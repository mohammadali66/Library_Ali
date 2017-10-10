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
  slugSubscription: Subscription;
  apiSubscription: Subscription;

  book: Book = new Book;
  pageNumber = 1;
  constructor(private bookService: BookService, private route: ActivatedRoute) { }

  ngOnInit() {
    //get slug from url
    this.slugSubscription = this.route.params.subscribe(
      (params: Params) => {
        this.book.slug = params['slug'];
      }
    );

    //get book from API
    this.apiSubscription = this.bookService.getBookDetail(this.book.slug)
      .subscribe(
        (bookData) => {
          this.book.title = bookData.title;
          this.book.category = bookData.category;
          this.book.authors = bookData.authors;
          this.book.publisher = bookData.publisher;
          this.book.pageCount = bookData.pageCount;
          this.book.description = bookData.description;
          this.book.image = bookData.image;
          this.book.pdfFile = bookData.pdfFile;
          this.book.featured = bookData.featured;
        },
        (error) => console.log(error)
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
    this.slugSubscription.unsubscribe();
    this.apiSubscription.unsubscribe();
  }

}