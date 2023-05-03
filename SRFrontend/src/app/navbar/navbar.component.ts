import { Component, OnDestroy } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../user/services/user.service';
import { BehaviorSubject, Subscription } from 'rxjs';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnDestroy{
  subscriptions: Subscription[] = []
  loggedIn = false

  constructor(public router: Router, private _userService: UserService) {
    this.subscriptions.push(this._userService.user$.subscribe(user => this.loggedIn = user !== null))
  }

  ngOnDestroy() {
    this.subscriptions.forEach(sub => sub.unsubscribe())
  }
}
