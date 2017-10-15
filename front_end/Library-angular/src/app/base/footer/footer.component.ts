import { Component, OnInit } from '@angular/core';

import { CategoryService } from '../../category/category.service';
import { Category } from '../../models/category.model';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

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
