import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../services/user.service';
import { catchError, take } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  registerForm = new FormGroup({
    email: new FormControl('', { nonNullable: true ,validators: Validators.required }),
    password: new FormControl('', { nonNullable: true, validators: Validators.required})
  })

  constructor(private _userService: UserService, private _router: Router) {}

  register() {
    this.registerForm.markAllAsTouched()
    if (!this.registerForm.valid) {
      return
    }
    
    this._userService.register(this.registerForm.getRawValue()).pipe(take(1),catchError(error => {
      throw error.error.detail;
    })
    ).subscribe(() => this._router.navigate(['/user/login']))
  }
}
