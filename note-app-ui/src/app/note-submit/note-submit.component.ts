import { Component, OnInit } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-note-submit',
  templateUrl: './note-submit.component.html',
  styleUrls: ['./note-submit.component.scss']
})
export class NoteSubmitComponent implements OnInit {
  public titleValue;
  public noteValue;
  @Output() newItemEvent = new EventEmitter<string>();
  constructor(public apiService:ApiService) { }

  ngOnInit(): void {
  }
  pushNote(){
    console.log("value here",this.titleValue,this.noteValue)
    let payloads = {'title':this.titleValue,
  'content':this.noteValue}
    this.apiService.pushNote(payloads)
          .subscribe((data)=>{
            console.log(data);
            this.writeEventEmitter("Your note sucessfully writed 📝");
            
          },error  => {
            console.log(error)
            this.writeEventEmitter("Failed to write your note: pls check payloads 🔴");
            
            });

  }
  writeEventEmitter(str){
    console.log("---- write issue ---")
    this.newItemEvent.emit(str);
  }

}
