import { LibraryAngularPage } from './app.po';

describe('library-angular App', () => {
  let page: LibraryAngularPage;

  beforeEach(() => {
    page = new LibraryAngularPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
