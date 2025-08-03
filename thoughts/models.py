from django.db import models
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

# Thought model to represent user thoughts
# Similar to a tweet, but can be chained to create a thread of thoughts
class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thoughts')
    content = models.TextField(max_length=280)  # Similar to a tweet
    created_at = models.DateTimeField(auto_now_add=True)

    # Posts can be chained to create a thread of thoughts
    chained_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='replies_in_chain'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

class ThoughtLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'thought')  # Prevent double likes

# Comment model to allow users to comment on thoughts
# Comments can also be nested to create a thread of comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# SharedThought model to allow users to share thoughts with others
# Shared thoughts are user-specific and can be shared multiple times
class SharedThought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# PinnedThought model to allow users to pin thoughts for easy access
# Pinned thoughts are user-specific and can be unpinned
class PinnedThought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'thought')


# ThoughtAttachment model to allow users to attach images to thoughts
# Attachments are user-specific and can be associated with a thought
class ThoughtAttachment(models.Model):
    thought = models.ForeignKey('Thought', related_name='attachments', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='thought_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for Thought {self.thought.id}"



@require_POST
@csrf_exempt  # You may replace this with @login_required + proper CSRF protection later
def upload_thought_images(request, thought_id):
    try:
        thought = Thought.objects.get(pk=thought_id)
    except Thought.DoesNotExist:
        return JsonResponse({'error': 'Thought not found.'}, status=404)

    files = request.FILES.getlist('image')
    current_count = thought.attachments.count()
    
    if current_count + len(files) > 5:
        return JsonResponse({'error': 'You can upload a maximum of 5 images per Thought.'}, status=400)

    for f in files:
        ThoughtAttachment.objects.create(thought=thought, image=f)

    return JsonResponse({'message': 'Images uploaded successfully.'})


    # <script src="https://kit.fontawesome.com/b8c639f9b4.js" crossorigin="anonymous"></script>