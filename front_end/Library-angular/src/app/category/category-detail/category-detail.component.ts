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

  constructor(private categoryService: CategoryService, private route: ActivatedRoute) { }

  ngOnInit() {
    //get category slug from url
    this.route.params.subscribe(
      (params: Params) => {
        //console.log(params['categoryslug']);
        this.category.slug = params['categoryslug'];
      }
    );
    console.log("Allllllllllllllllllll");

    //get category from API
    this.categoryService.getOneCategoryByBooks(this.category.slug)
      .subscribe(
        (categoryData) => {
          this.category.name = categoryData.name;
          this.category.description = categoryData.description;

          let books: Array<Book> = new Array<Book>();
          for(const b of categoryData.category_books){
            let book: Book = new Book;
            book.title = b.title;
            book.slug = b.slug;
            book.category = this.category;
            book.authors = b.authors;
            book.publisher = b.publisher;
            book.pageCount = b.pageCount;
            book.description = b.description;
            book.image = b.image;
            book.pdfFile = b.pdfFile;
            book.featured = b.featured;

            books.push(book);
          }
          this.category.category_books = books
        },
        (error) => console.log(error)
      );
  }

}
