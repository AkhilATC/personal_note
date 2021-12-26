import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'note-app-ui';
  public message = "Welcome to jOtter 📓. You can write what you ❤️"
  ngOnInit(): void {
  }
  addItem(newItem: string){
    console.log("-------gggg-----")
    this.ngOnInit()
    this.message = newItem
   

  }
}
