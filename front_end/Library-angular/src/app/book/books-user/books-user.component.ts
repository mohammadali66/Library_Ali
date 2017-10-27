import { Component, OnInit } from '@angular/core';

import { BookService } from '../book.service';
import { Book } from '../../models/book.model';

@Component({
  selector: 'app-books-user',
  templateUrl: './books-user.component.html',
  styleUrls: ['./books-user.component.css']
})
export class BooksUserComponent implements OnInit {

  bookList: Array<Book>;
  previous: string = null;
  next: string = null;

  constructor(private bookService: BookService) { }

  ngOnInit() {
    this.bookService.booksOfLoggedUser()
      .subscribe(
        (data: any) => {
          this.bookList = new Array<Book>();
          for(let b of data.results){
            let book: Book = new Book();
            book.title = b.title;
            book.slug = b.slug;
            book.authors = b.authors;
            book.image = b.image;
            book.featured = b.featured;

            this.bookList.push(book);
          }
          this.previous = data.previous;
          this.next = data.next;
          //console.log(this.bookList);
        }
      );
  }

  //........................................................................
    nextPage(which: string){
      let pageUrl = '';
      if(which === 'next'){
        pageUrl = this.next;
      }else if(which === 'previous'){
        pageUrl = this.previous;
      }
      this.bookService.booksOfLoggedUser(pageUrl)
        .subscribe(
          (data: any) => {

            this.bookList = new Array<Book>();
            for(let b of data.results){
              let book: Book = new Book();
              book.title = b.title;
              book.slug = b.slug;
              book.authors = b.authors;
              book.image = b.image;
              book.featured = b.featured;

              this.bookList.push(book);
            }

            this.previous = data.previous;
            this.next = data.next;
          },
          (error) => console.log(error)
        );
    }
}
