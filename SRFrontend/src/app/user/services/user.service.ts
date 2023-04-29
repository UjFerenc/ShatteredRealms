import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { UserLoginInfo } from '../models/interface.userlogininfo';
import { HttpClient } from '@angular/common/http'
import { User } from '../models/interface.user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  login(user: UserLoginInfo): Observable<User> {
    return this.http.post<User>('', user)
  }
}
