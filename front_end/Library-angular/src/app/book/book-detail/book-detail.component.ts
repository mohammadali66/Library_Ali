import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Subscription } from 'rxjs/Subscription';

import { BookService } from '../book.service';
import { NoteService } from '../../note/note.service';
import { Book } from '../../models/book.model';
import { Note } from '../../models/note.model';

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
  //pdfFilePath: string;
  isLoggedUser = false;
  message = '';

  constructor(private bookService: BookService,
              private noteService: NoteService,
              private route: ActivatedRoute,
              private router: Router) { }


  function_for_ngOnInit(){
    //get slug from url
    this.route.params.subscribe(
      (params: Params) => {
        this.book = new Book;
        this.book.slug = params['slug'];

        //get book from API
        this.bookService.getBookDetail(this.book.slug)
          .subscribe(
            (bookData) => {
              //console.log(bookData);
              this.message = '';

              this.book.title = bookData.title;
              this.book.slug = bookData.slug;
              this.book.description = bookData.description;
              this.book.authors = bookData.authors;
              this.book.publisher = bookData.publisher;
              this.book.pageCount = bookData.pageCount;
              this.book.image = bookData.image;

              this.book.pdfFile = bookData.pdfFile;
              //this.pdfFilePath = this.bookService.mainUrl + bookData.pdfFile;

              //this.book.featured = bookData.featured;
              this.book.category.name = bookData.category.name;
              this.book.category.slug = bookData.category.slug;

              if(bookData.notes){
                this.book.notes = new Array<Note>();
                for(let n of bookData.notes){
                  let note: Note = new Note();
                  note.id = n.id;
                  note.text = n.text;
                  note.pageOfBook = n.pageOfBook;
                  note.created_datetime = n.created_datetime;
                  note.updated_datetime = n.updated_datetime;
                  this.book.notes.push(note);
                }
              }

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

  ngOnInit() {
    this.function_for_ngOnInit();
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

  addBook(){
    this.bookService.addBookToBooksListUser(this.book.slug)
      .subscribe(
        (data) => {
          console.log(data);

          //a trick for reloading current component
          //this.router.navigate(['/']);
          //this.router.navigate(['/book', this.book.slug]);
          //this.router.navigateByUrl(this.router.url);
          //window.location.reload();
          this.function_for_ngOnInit();   //reload the component
        }
      );
  }


  deleteNote(noteId){
    this.noteService.deleteNote(noteId)
    .subscribe(
      (data) => {
        this.message = 'The note has deleted successfully!';
        //a trick for reloading current component
        // this.router.navigate(['blank']);
        // this.router.navigate(['/book', this.book.slug]);
        //window.location.reload();
        this.function_for_ngOnInit(); //reload the component
      }
    );
  }

  ngOnDestroy(){
    //this.slugSubscription.unsubscribe();
    //this.apiSubscription.unsubscribe();
  }

}
