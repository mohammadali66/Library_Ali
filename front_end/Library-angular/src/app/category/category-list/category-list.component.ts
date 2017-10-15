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

  constructor(private categoryService: CategoryService) {

  }

  ngOnInit() {
    this.categoryApiSubscription = this.categoryService.getCategoryBooksHomeList()
      .subscribe(
        (categoryData: any) => {
          
          for(const cat of categoryData.results){
            let category: Category = new Category;
            category.name = cat.name;
            category.slug = cat.slug;

            let books: Array<Book> = new Array<Book>();
            for(const b of cat.books){
              let book: Book = new Book;
              book.title = b.title;
              book.slug = b.slug;
              book.image = b.image;
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
    //this.categoryApiSubscription.unsubscribe();
  }
}
