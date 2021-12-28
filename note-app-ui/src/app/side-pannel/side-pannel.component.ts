import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-side-pannel',
  templateUrl: './side-pannel.component.html',
  styleUrls: ['./side-pannel.component.scss']
})
export class SidePannelComponent implements OnInit {
  public data:any = []
 
  constructor(public apiService:ApiService) { }

  ngOnInit(): void {
    this.bindNotes()

  }
  bindNotes(){
     this.apiService.getLatestNotes().subscribe((data)=>{
       console.log("here data---->>>",data)
      this.data = data
    })
  }
  
  deleteNote(node){
    console.log(node)
    this.apiService.deleteNote(node.id)
          .subscribe((data)=>{
            console.log(data);
            this.bindNotes();
          },error  => {
            console.log(error)            
            });
  }

  
  

}
