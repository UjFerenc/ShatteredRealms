import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { take } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  emailControl = new FormControl('', Validators.required)
  passwordControl = new FormControl('', Validators.required)

  loginForm2 = new FormGroup({
    email: this.emailControl,
    password: this.passwordControl
  })


  loginForm = new FormGroup({
    email: new FormControl('', { nonNullable:true, validators: Validators.required }),
    password: new FormControl('', { nonNullable: true, validators: Validators.required }),
  });

  constructor(private _userService: UserService, private _router: Router) { }

  login() {
    if (!this.loginForm.valid) {
      return
    }
    
    this._userService.login(this.loginForm.getRawValue()).pipe(take(1))
      .subscribe(() => this._router.navigate(['/user/profile']))
  }
}
