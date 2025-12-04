from django.db import models


class GameDate(models.Model):
    year = models.IntegerField()
    day_of_the_year = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["year", "day_of_the_year"], name="unique_date"),
            models.CheckConstraint(
                condition=models.Q(day_of_the_year__gte=1) & models.Q(day_of_the_year__lte=365),
                name="days_range_constraint",
                violation_error_message="days must be in range 1-365",
            ),
        ]

    def __str__(self):
        return f"{self.year} - {self.day_of_the_year:03d}"
