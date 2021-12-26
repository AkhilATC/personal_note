import { Component, ViewChild } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { SidePannelComponent } from './side-pannel/side-pannel.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'note-app-ui';
  public message = "Welcome to jOtter 📓. You can write what you ❤️"
  public currentItem:boolean = false;
 
  @ViewChild(SidePannelComponent) child:SidePannelComponent;
  public constructor(private router: Router) {}
  ngOnInit(): void {
    
  }
  addItem(newItem: string){
    
    this.message = newItem
    this.child.bindNotes()
  }
}
