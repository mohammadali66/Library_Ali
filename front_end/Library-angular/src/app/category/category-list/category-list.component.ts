import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';

import { Category } from '../../models/category.model';
import { Book } from '../../models/book.model';
import { CategoryService } from '../category.service';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit, OnDestroy {

  categoryApiSubscription: Subscription;
  categoryList: Array<Category> = new Array<Category>();

  constructor(private categoryService: CategoryService) { }

  ngOnInit() {

    this.categoryApiSubscription = this.categoryService.getCategoryList()
      .subscribe(
        (categoryData) => {

          for(const cat of categoryData){
            let category: Category = new Category;
            category.name = cat.name;
            category.slug = cat.slug;

            let books: Array<Book> = new Array<Book>();
            for(const b of cat.category_books){
              let book: Book = new Book;
              book.title = b.title;
              book.slug = b.slug;
              book.category = category;
              book.authors = b.authors;
              book.publisher = b.publisher;
              book.pageCount = b.pageCount;
              book.description = b.description;
              book.image = b.image;
              book.pdfFile = b.pdfFile;
              book.featured = b.featured;

              books.push(book);
            }
            category.category_books = books;
            this.categoryList.push(category);
          }
        },
        (error) => console.log(error)
      );


  }

  ngOnDestroy(){
    this.categoryApiSubscription.unsubscribe();
  }
}
