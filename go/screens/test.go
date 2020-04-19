package screens

import (
	"fmt"
	"time"

	"fyne.io/fyne"
	"fyne.io/fyne/canvas"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/theme"
	"fyne.io/fyne/widget"
)

func makeProjectTab() fyne.Widget {
	return widget.NewVBox(
		widget.NewButton("Launch", func() {}),
		widget.NewGroup(
			"Product",
			widget.NewSelect([]string{"debug", "release"}, func(s string) { fmt.Println("selected", s) }),
			fyne.NewContainerWithLayout(layout.NewAdaptiveGridLayout(2),
				widget.NewButton("Clean", func() {}),
				widget.NewButton("Build", func() {}),
			),
		),
		widget.NewGroup(
			"Settings",
			widget.NewButton("Open", func() {}),
		),
	)
}

func makeRomTab() fyne.Widget {
	return widget.NewVBox(
		widget.NewGroup(
			"Archive",
			widget.NewSelect([]string{"Enterprise", "Adhoc", "Master"},
				func(s string) {
					fmt.Println("selected", s)
				}),
			fyne.NewContainerWithLayout(layout.NewAdaptiveGridLayout(2),
				widget.NewButton("Clean", func() {}),
				widget.NewButton("Build", func() {}),
			),
		),
		widget.NewGroup(
			"Settings",
			widget.NewButton("Open", func() {}),
		),
	)
}

func makeProgressTab() fyne.Widget {
	progress := widget.NewProgressBar()
	infProgress := widget.NewProgressBarInfinite()

	go func() {
		num := 0.0
		for num < 1.0 {
			time.Sleep(100 * time.Millisecond)
			progress.SetValue(num)
			num += 0.01
		}

		progress.SetValue(1)
	}()

	return widget.NewVBox(
		widget.NewLabel("Percent"), progress,
		widget.NewLabel("Infinite"), infProgress)
}

func makeFormTab() fyne.Widget {
	name := widget.NewEntry()
	name.SetPlaceHolder("John Smith")
	email := widget.NewEntry()
	email.SetPlaceHolder("test@example.com")
	password := widget.NewPasswordEntry()
	password.SetPlaceHolder("Password")
	largeText := widget.NewMultiLineEntry()

	form := &widget.Form{
		OnCancel: func() {
			fmt.Println("Cancelled")
		},
		OnSubmit: func() {
			fmt.Println("Form submitted")
			fmt.Println("Name:", name.Text)
			fmt.Println("Email:", email.Text)
			fmt.Println("Password:", password.Text)
			fmt.Println("Message:", largeText.Text)
		},
	}
	form.Append("Name", name)
	form.Append("Email", email)
	form.Append("Password", password)
	form.Append("Message", largeText)

	return form
}

func makeScrollTab() fyne.CanvasObject {
	logo := canvas.NewImageFromResource(theme.FyneLogo())
	logo.SetMinSize(fyne.NewSize(320, 320))
	list := widget.NewHBox()
	list2 := widget.NewVBox()

	for i := 1; i <= 20; i++ {
		index := i // capture
		list.Append(widget.NewButton(fmt.Sprintf("Button %d", index), func() {
			fmt.Println("Tapped", index)
		}))
		list2.Append(widget.NewButton(fmt.Sprintf("Button %d", index), func() {
			fmt.Println("Tapped", index)
		}))
	}

	horiz := widget.NewScrollContainer(list)
	vert := widget.NewScrollContainer(list2)

	scrolls := fyne.NewContainerWithLayout(layout.NewBorderLayout(horiz, nil, nil, nil),
		horiz, vert)
	return fyne.NewContainerWithLayout(layout.NewAdaptiveGridLayout(2), scrolls, makeScrollBothTab())
}

func makeScrollBothTab() fyne.CanvasObject {
	logo := canvas.NewImageFromResource(theme.FyneLogo())
	logo.SetMinSize(fyne.NewSize(800, 800))

	scroll := widget.NewScrollContainer(logo)
	scroll.Resize(fyne.NewSize(400, 400))

	return scroll
}

// TestScreen shows a panel containing widget demos
func TestScreen() fyne.CanvasObject {
	return fyne.NewContainerWithLayout(layout.NewBorderLayout(nil, nil, nil, nil),
		widget.NewTabContainer(
			widget.NewTabItem("Project", makeProjectTab()),
			widget.NewTabItem("Rom", makeRomTab()),
			widget.NewTabItem("Progress", makeProgressTab()),
			widget.NewTabItem("Form", makeFormTab()),
			widget.NewTabItem("Scroll", makeScrollTab()),
		),
	)
}
