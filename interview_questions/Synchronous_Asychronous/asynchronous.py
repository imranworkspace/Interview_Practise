import asyncio

async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(5)
    print(f"Finished {name}")

async def main():
    await asyncio.gather(
        task("Task 1"),
        task("Task 2"),
        task("Task 3")
    )

asyncio.run(main()) 


class Blog(models.Model):
    blog = models.CharField(max_length=25)
    desc = models.TextField()

class Author(models.Model):
    author = models.CharField(max_length=25)

class Entry(models.Model):
    blog = models.Foreignkey(Blog,on_delete=models.CASCADE)
    headlines = models.TextField()
    author = models.ManyToMany(author)

# hit again and again
e = Entry.objects.get(id=5)
e.blog

# hit only one time 
e=Blog.objects.sellect_related('blog').get(id=5)
b=e.blog




