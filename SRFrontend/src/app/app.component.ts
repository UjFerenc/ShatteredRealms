import { Component } from '@angular/core';
import { signal } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'SRFrontend';
  asd = signal<string>('asd')
}
