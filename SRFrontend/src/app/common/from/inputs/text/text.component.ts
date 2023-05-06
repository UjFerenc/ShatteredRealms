import { Component, Input, OnDestroy } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { debounceTime, startWith, Subscription } from 'rxjs';

@Component({
  selector: 'app-form-input-text',
  templateUrl: './text.component.html',
  styleUrls: ['./text.component.scss'],
})
export class TextComponent implements OnDestroy {
  @Input() set formInput(formInput: FormControl) {
    this._formInput = formInput;
    this.subscriptions.push(
      this._formInput.valueChanges
        .pipe(debounceTime(300), startWith(''))
        .subscribe((data) => {
          if (this._formInput.errors)
            [this.errorKey, this.error] = Object.entries(
              this._formInput.errors
            )[0];
          this.error = { ...this.error, field_name: this.label };
        })
    );
    this.required = this._formInput.hasValidator(Validators.required);
  }
  get formInput() {
    return this._formInput;
  }

  _formInput = new FormControl();
  @Input() label: string | null = null;
  @Input() placeholder: string = '';
  @Input() type: string | null = null;
  @Input() helper: string | null = null;
  errorKey: string = '';
  error: any = {};

  required = false;

  subscriptions: Subscription[] = [];

  ngOnDestroy(): void {
    this.subscriptions.forEach((sub) => {
      sub.unsubscribe();
    });
  }
}
