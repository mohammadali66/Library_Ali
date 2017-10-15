import { Component, OnInit } from '@angular/core';

import { CategoryService } from '../../category/category.service';
import { Category } from '../../models/category.model';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {

  categoryList: Array<Category> = new Array<Category>();

  constructor(private categoryService: CategoryService) { }

  ngOnInit() {
    this.categoryService.getCategoryMenu().subscribe(
      (categoryData: any) => {
        //console.log(categoryData.results);
        for(const cat of categoryData.results){
          let category: Category = new Category;
          category.name = cat.name;
          category.slug = cat.slug;
          this.categoryList.push(category);
        }
         //console.log("categories:" + this.categoryList)
      }
    );
  }

}
