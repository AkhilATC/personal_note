import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-note-submit',
  templateUrl: './note-submit.component.html',
  styleUrls: ['./note-submit.component.scss']
})
export class NoteSubmitComponent implements OnInit {
  public titleValue;
  public noteValue;
  constructor() { }

  ngOnInit(): void {
  }
  pushNote(){
    console.log("value here",this.titleValue,this.noteValue)

  }

}
