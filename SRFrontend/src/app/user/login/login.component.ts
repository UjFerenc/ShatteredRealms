import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { take } from 'rxjs';

import { TranslateService } from '@ngx-translate/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  loginForm = new FormGroup({
    email: new FormControl('', {
      nonNullable: true,
      validators: [Validators.required, Validators.email],
    }),
    password: new FormControl('', {
      nonNullable: true,
      validators: [Validators.required, Validators.minLength(8)],
    }),
  });

  constructor(
    private _userService: UserService,
    private _router: Router,
    public translateService: TranslateService
  ) {}

  login() {
    if (!this.loginForm.valid) {
      return;
    }

    this._userService
      .login(this.loginForm.getRawValue())
      .pipe(take(1))
      .subscribe(() => this._router.navigate(['/user/profile']));
  }
}
