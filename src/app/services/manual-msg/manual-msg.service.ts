import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ManualMsgService {

  constructor(private http: HttpClient) { }

  public manualmsgs(data){
    var res=this.http.post("http://localhost:5000/manual-generate",data);
    return res;
  }
}
