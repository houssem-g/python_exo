class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = 0
        self.currentPage = 0
        self.getPageSize()
    def getItems(self):
        return self.items
		
    def getPageSize(self):

        if len(self.items) > 0:
            n = self.pageSize
            self.items = [self.items[i * n:(i + 1) * n] for i in range((len(self.items) + n - 1) // n )]
            self.totalPages = len(self.items)
        return self.pageSize
		
    def getCurrentPage(self):
        return self.currentPage
    def prevPage(self):
        self.currentPage = self.currentPage - 1 if self.currentPage > 1 else self.currentPage
        return self
    def nextPage(self):
        self.currentPage = self.currentPage + 1 if self.currentPage < self.totalPages else self.currentPage
        return self
    def firstPage(self):
        self.currentPage = 1
        return self
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
    def goToPage(self, page):
        page = int(page)
        self.currentPage = page
        if page < 0:
            self.currentPage = 1
        elif page > self.totalPages:
            self.currentPage = self.totalPages
        return self
    def getVisibleItems(self):
        
        return self.items[self.currentPage-1]


# defaultPagination = Pagination()
# p1 = Pagination([None]*69, 5)
# print("getPageSize: ", p1.getPageSize())
# print("nextPage.getCurrentPage: ", p1.nextPage().getCurrentPage())
# ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p1 = Pagination([None]*69, 5)
print("goToPage: ", p1.goToPage( 99).getCurrentPage())
print("goToPage: ", p1.goToPage( 4).getCurrentPage())
print("goToPage: ", p1.goToPage(6.5).getCurrentPage())
print("goToPage: ", p1.goToPage(-99).getCurrentPage())
