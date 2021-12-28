import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpResponse, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }
  public api_base_url = "http://localhost:7001/my_note_space"
  public getLatestNotes(){
    return this.httpClient.get(`${this.api_base_url}/fetch_notes`);
  };

  public pushNote(payload){
    //let params = new HttpParams();
      console.log("--- SENDing API ---")
      let response = this.httpClient.post(`${this.api_base_url}/write_note`,
      payload
      )
      return response;
  }
  public deleteNote(id){

    let response = this.httpClient.delete(`${this.api_base_url}/${id}/erase_note`, 
      )
      return response;

  }
}
