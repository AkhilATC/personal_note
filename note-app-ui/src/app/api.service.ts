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
}
