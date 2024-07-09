import { Component, computed, OnDestroy, Signal } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';

import { UserService } from '../user/services/user.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
})
export class NavbarComponent implements OnDestroy {
  subscriptions: Subscription[] = [];
  loggedIn: Signal<boolean>;

  constructor(public router: Router, private _userService: UserService) {
    this.loggedIn = computed(() => this._userService.user() !== null);
  }

  ngOnDestroy() {
    this.subscriptions.forEach((sub) => sub.unsubscribe());
  }
}
