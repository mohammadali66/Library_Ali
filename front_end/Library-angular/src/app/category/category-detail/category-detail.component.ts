import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';

import { Category } from '../../models/category.model';
import { Book } from '../../models/book.model';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category-detail',
  templateUrl: './category-detail.component.html',
  styleUrls: ['./category-detail.component.css']
})
export class CategoryDetailComponent implements OnInit {

  category: Category = new Category;
  previous: string = null;
  next: string = null;

  constructor(private categoryService: CategoryService, private route: ActivatedRoute) { }

  ngOnInit() {
    //get category slug from url ...............................
    this.route.params.subscribe(
      (params: Params) => {
        this.category.slug = params['categoryslug'];

        //get category detail information from API ..............
        this.categoryService.getOneCategoryBrief(this.category.slug)
          .subscribe(
            (data: any) => {
              this.category.name = data.name;              
            }
          );

        //get books list of category from API ...................
        this.categoryService.getBooksOfOneCategory(this.category.slug)
          .subscribe(
            (data: any) => {

              this.category.category_books = new Array<Book>();
              for(let b of data.results){
                let book: Book = new Book();
                book.title = b.title;
                book.slug = b.slug;
                book.authors = b.authors;
                book.image = b.image;
                book.featured = b.featured;

                this.category.category_books.push(book);
              }
              this.previous = data.previous;

              this.next = data.next;
            },
            (error) => console.log(error)
          );
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
    this.categoryService.getBooksOfOneCategory(this.category.slug, pageUrl)
      .subscribe(
        (data: any) => {

          this.category.category_books = new Array<Book>();
          for(let b of data.results){
            let book: Book = new Book();
            book.title = b.title;
            book.slug = b.slug;
            book.authors = b.authors;
            book.image = b.image;
            book.featured = b.featured;

            this.category.category_books.push(book);
          }
          this.previous = data.previous;
          this.next = data.next;
        },
        (error) => console.log(error)
      );
  }
}
