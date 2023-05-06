import { HttpClient } from '@angular/common/http';
import { Injectable, signal } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { environment } from 'src/app/environments/environment';

import { User } from '../models/interface.user';
import { UserLoginInfo } from '../models/interface.userlogininfo';

@Injectable()
export class UserService {
  user = signal<User | null>(null);

  constructor(private http: HttpClient) {
    let currentUser = localStorage.getItem('userService/user');
    this.user = signal(currentUser ? JSON.parse(currentUser) : null);
  }

  login(user: UserLoginInfo): Observable<User> {
    return this.http.post<User>(environment.APIUri + '/user/login', user).pipe(
      tap((user: User) => {
        this.user.set(user);
      })
    );
  }

  register(user: UserLoginInfo): Observable<void> {
    return this.http.post<void>(environment.APIUri + '/user/register', user);
  }

  logout() {
    this.user.set(null);
  }
}
