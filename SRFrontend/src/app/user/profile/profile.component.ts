import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent {
  constructor(private _userService: UserService, private _router: Router) {}
  
  logout() {
    this._userService.logout();
    this._router.navigate(['/user/login'])
  }
}
