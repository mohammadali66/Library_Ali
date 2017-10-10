import { Book } from './book.model';


export class Category{

  public name: string;
  public slug: string;
  public description: string;
  public category_books: Book[];

  constructor(){}
}
