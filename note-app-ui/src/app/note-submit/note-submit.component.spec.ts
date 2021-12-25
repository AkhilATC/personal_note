import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NoteSubmitComponent } from './note-submit.component';

describe('NoteSubmitComponent', () => {
  let component: NoteSubmitComponent;
  let fixture: ComponentFixture<NoteSubmitComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NoteSubmitComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NoteSubmitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
