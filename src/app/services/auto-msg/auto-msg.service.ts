import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AutoMsgService {

  constructor(private http: HttpClient) { }

  public generatemsgs(data){
    var res=this.http.post("http://localhost:5000/auto-generate",data);
    return res;
  }

  public stopmsgs(data){
    var res=this.http.post("http://localhost:5000/auto-stop",data);
    return res;
  }
}
