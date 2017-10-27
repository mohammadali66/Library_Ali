import { Component, OnInit, Input } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

import { NoteService } from '../note.service';

@Component({
  selector: 'app-note-create',
  templateUrl: './note-create.component.html',
  styleUrls: ['./note-create.component.css']
})
export class NoteCreateComponent implements OnInit {

  @Input() bookSlug = 'empty';
  successMessage = '';
  errorMessage = '';

  constructor(private noteService: NoteService,
              private router: Router) { }

  ngOnInit() {
  }

  addNote(form: NgForm){
    let note = {
      text: form.value.textNote,
      pageOfBook: form.value.pageofbook
    }
    //console.log(note);
    this.noteService.createNote(this.bookSlug, note)
      .subscribe(
        (data: any[]) => {
          //console.log(data);
          this.successMessage = "Your note have been added, successfully.";
          this.errorMessage = '';
        },
        (error) => {
          this.errorMessage = "error in process!!";
          this.successMessage = '';
        }
      );
      
      //a trick for reloading current component
      // this.router.navigate(['blank']);
      // this.router.navigate(['/book', this.bookSlug]);
      //window.location.reload();
  }
}
