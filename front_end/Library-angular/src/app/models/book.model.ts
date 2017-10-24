import { Category } from './category.model';
import { Note } from './note.model';

export class Book{

  public title: string;
  public slug: string;

  public category: Category;
  public notes: Array<Note>;

  public authors: string;
  public publisher: string;
  public pageCount: number;
  public description: string;
  public image: string;
  public pdfFile: string;
  public featured: Boolean;
  constructor() {
    this.category = new Category;
  }
}
