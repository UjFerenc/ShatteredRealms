import { BehaviorSubject, Observable, Subject, Subscription, catchError, take, tap } from 'rxjs';
import { UserLoginInfo } from '../models/interface.userlogininfo';
import { HttpClient } from '@angular/common/http';
import { User } from '../models/interface.user';
import { environment } from 'src/app/environments/environment';
import { Injectable, OnDestroy } from '@angular/core';

@Injectable()
export class UserService implements OnDestroy{
  subscriptions: Subscription[] = []

  user$ = new BehaviorSubject<User | null>(null);

  constructor(private http: HttpClient) {
    let currentUser = localStorage.getItem('userService/user')
    if (currentUser !== null) this.user$.next(JSON.parse(currentUser));

    this.subscriptions.push(this.user$.subscribe(user => {
      if (user === null) {
        localStorage.removeItem('userService/user')
        return
      }

      localStorage.setItem('userService/user', JSON.stringify(user));
    }))
  }

  login(user: UserLoginInfo): Observable<User> {
    return this.http.post<User>(environment.APIUri + '/user/login', user).pipe(
      tap((user: User) => {
        this.user$.next(user);
      })
    );
  }

  register(user: UserLoginInfo): Observable<void> {
    return this.http.post<void>(environment.APIUri+'/user/register', user);
  }

  logout() {
    this.user$.next(null)
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub=> sub.unsubscribe())
  }
}
